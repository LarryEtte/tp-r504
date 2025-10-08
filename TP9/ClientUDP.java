import java.io.*;
import java.net.*;

public class ClientUDP {
    public static void main(String[] args) throws Exception {
        InetAddress addr = InetAddress.getLocalHost();
		System.out.println("adresse="+addr.getHostName());
        String s = "Hello World";
        byte[] data = s.getBytes();
        DatagramSocket sock = new DatagramSocket();
        DatagramPacket packet = new DatagramPacket(data, data.length, addr, 1234);
        sock.send(packet);
        byte[] buffer = new byte[1024];
        DatagramPacket rec = new DatagramPacket(buffer, buffer.length);
        sock.receive(rec);
        String received = new String(rec.getData(), 0, rec.getLength());
        System.out.println("Réponse du serveur : " + received);
        sock.close();
    }
}
