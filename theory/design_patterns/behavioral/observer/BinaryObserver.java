public class BinaryObserver extends Observer {
    @Override
    public void update() {
        System.out.println("Binary String: "+ Integer.toBinaryString(subject.getState()));
    }
}
