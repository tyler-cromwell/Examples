public class Client {
    public static ConcreteCommand createConcreteCommand(Receiver r) {
        return new ConcreteCommand(r);
    }

    public static void main(String[] args) {
        Invoker invoker = new Invoker();
        Receiver receiver = new Receiver();

        Command command = createConcreteCommand(receiver);
        invoker.storeCommand(command);
        invoker.invoke();
    }
}
