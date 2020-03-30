public class Client {
    public static void main(String[] args) {
        AbstractFactory factory = new ConcreteFactory();
        AbstractProduct product = factory.createProduct();

        System.out.println(product);
    }
}
