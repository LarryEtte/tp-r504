import java.io.*;
import java.net.*;

public class ServeurUDP {
    public static void main(String[] args) throws Exception {
        DatagramSocket sock = new DatagramSocket(1234);
        byte[] buffer = new byte[1024];
        while (true) {
            System.out.println("- Waiting for data");
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            sock.receive(packet);
            String str = new String(packet.getData(), 0, packet.getLength());
            System.out.println("Reçu : " + str);
            byte[] data = str.getBytes();
            InetAddress clientAddr = packet.getAddress();
            int clientPort = packet.getPort();
            DatagramPacket response = new DatagramPacket(data, data.length, clientAddr, clientPort);
            sock.send(response);
        }
    }
}
