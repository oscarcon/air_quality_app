import javax.ws.rs.client.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
public class Demo {
    public static void main(String[] args) {
        Client client = ClientBuilder.newClient();
        WebTarget webTarget = client.target("http://127.0.0.1:5000");
        WebTarget resource = webTarget.path("/");
        Invocation.Builder invokBuilder = resource.request(MediaType.APPLICATION_JSON);
        Response response = invokBuilder.get();
        System.out.println(response.getStatus());
        System.out.println(response.readEntity(String.class));

    }
}