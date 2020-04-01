public class Product {
    private String name;
    private String description;

    public Product(String n) {
        this.name = n;
    }

    public Product(String n, String d) {
        this.name = n;
        this.description = d;
    }

    public void setName(String n) {
        this.name = n;
    }

    public void setDescription(String d) {
        this.description = d;
    }

    public String getName() {
        return this.name;
    }

    public String getDescription() {
        return this.description;
    }
}
