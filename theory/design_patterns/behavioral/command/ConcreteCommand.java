public class ConcreteCommand implements Command {
    private Receiver receiver;

    public ConcreteCommand(Receiver r) {
        this.receiver = r;
    }

    @Override
    public void execute() {
        this.receiver.action();
    }
}
