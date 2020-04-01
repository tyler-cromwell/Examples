public class ProductBuilder implements Builder {
    private Product product;

    public void buildProduct(String name, String description) {
        this.product = new Product(name, description);
    }

    public Product getProduct() {
        return this.product;
    }
}
