public class Client {
    public static void main(String[] args) {
        // Use a director to manage the building of an object
        Director director = new Director(new ProductBuilder());

        // Create the object step-by-step
        director.constructProduct();

        // Get the final result
        Product product = director.getResult();
        System.out.println(product.getName());
        System.out.println(product.getDescription());
    }
}
