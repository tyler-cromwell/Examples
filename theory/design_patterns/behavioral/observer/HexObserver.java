public class HexObserver extends Observer {
    @Override
    public void update() {
        System.out.println("Hex String: "+ Integer.toHexString(subject.getState()).toUpperCase());
    }
}
