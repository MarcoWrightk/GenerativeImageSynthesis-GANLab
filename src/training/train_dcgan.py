import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from architectures.dcgan import Generator, Discriminator

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
latent_dim = 100
G = Generator(latent_dim).to(device)
D = Discriminator().to(device)

criterion = torch.nn.BCELoss()
optimizer_G = torch.optim.Adam(G.parameters(), lr=0.0002)
optimizer_D = torch.optim.Adam(D.parameters(), lr=0.0002)

transform = transforms.Compose([
    transforms.Resize(64),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])
dataset = datasets.CIFAR10(root="./data", download=True, transform=transform)
loader = DataLoader(dataset, batch_size=64, shuffle=True)

for epoch in range(50):
    for real, _ in loader:
        real = real.to(device)
        batch_size = real.size(0)

        # Train Discriminator
        z = torch.randn(batch_size, latent_dim, 1, 1).to(device)
        fake = G(z)
        loss_D = criterion(D(real), torch.ones_like(D(real))) + \
                 criterion(D(fake.detach()), torch.zeros_like(D(fake)))
        optimizer_D.zero_grad()
        loss_D.backward()
        optimizer_D.step()

        # Train Generator
        loss_G = criterion(D(fake), torch.ones_like(D(fake)))
        optimizer_G.zero_grad()
        loss_G.backward()
        optimizer_G.step()

