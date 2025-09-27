def test_generator_shape():
    from src.architectures.dcgan import Generator
    model = Generator()
    z = torch.randn(1, 100, 1, 1)
    output = model(z)
    assert output.shape == (1, 3, 64, 64)
