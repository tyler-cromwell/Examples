public class ConcreteFactory implements AbstractFactory {
    public ConcreteProduct createProduct() {
        return new ConcreteProduct();
    }
}
