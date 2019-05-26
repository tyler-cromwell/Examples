class Singleton {
    private static Singleton singleton = null;
    private String data;

    private Singleton() {}

    private Singleton(String parameter) {
        this.data = parameter;
    }

    public static Singleton getInstance() {
        if (singleton == null) {
            singleton = new Singleton();
        }
        return singleton;
    }

    public static Singleton getInstance(String parameter) {
        if (singleton == null) {
            singleton = new Singleton();
        }
        return singleton;
    }

    public static void main(String args[]) {
        Singleton singleton = Singleton.getInstance();
        System.out.println(singleton);
    }
}
