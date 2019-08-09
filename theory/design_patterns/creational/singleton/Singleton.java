class Singleton {
    private static Singleton singleton = null;
    private String data = "";

    private Singleton() {}

    private Singleton(String parameter) {
        this.data = parameter;
    }

    @Override
    public String toString() {
        if (this.data == "" || this.data == null) {
            return super.toString();
        } else {
            return this.data;
        }
    }

    public static Singleton getInstance() {
        if (singleton == null) {
            singleton = new Singleton();
        }
        return singleton;
    }

    public static Singleton getInstance(String parameter) {
        if (singleton == null) {
            singleton = new Singleton(parameter);
        }
        return singleton;
    }

    public static void main(String args[]) {
        Singleton singleton = null;

        if (args.length > 0 && args[0] != null) {
            singleton = Singleton.getInstance(args[0]);
        } else {
            singleton = Singleton.getInstance();
        }

        System.out.println(singleton);
    }
}
