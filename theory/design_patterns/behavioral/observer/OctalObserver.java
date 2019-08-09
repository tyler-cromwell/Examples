public class OctalObserver extends Observer {
    @Override
    public void update() {
        System.out.println("Octal String: "+ Integer.toOctalString(subject.getState()));
    }
}
