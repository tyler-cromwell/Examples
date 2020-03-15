public class Invoker {
    private Command command;

    public void storeCommand(Command c) {
        this.command = c;
    }

    public void invoke() {
        this.command.execute();
    }
}
