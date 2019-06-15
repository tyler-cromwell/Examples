public abstract class Observer {
    protected Subject subject;
    public abstract void update();
    
    public void setSubject(Subject subject) {
        this.subject = subject;
    }

    public static void main(String[] args) {
        Subject subject = new Subject();

        subject.attach(new HexObserver());
        subject.attach(new OctalObserver());
        subject.attach(new BinaryObserver());

        System.out.println("First state change: 15");	
        subject.setState(15);
        System.out.println("Second state change: 10");	
        subject.setState(10);
    }
}
