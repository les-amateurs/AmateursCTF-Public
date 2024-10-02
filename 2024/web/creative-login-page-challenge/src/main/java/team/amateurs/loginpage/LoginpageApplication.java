package team.amateurs.loginpage;

import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.http.MediaType;
import org.springframework.security.crypto.bcrypt.BCrypt;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.bind.annotation.*;

import javax.print.attribute.standard.Media;
import java.io.IOException;
import java.lang.reflect.Field;
import java.nio.charset.Charset;
import java.util.Base64;
import java.util.HashMap;

@SpringBootApplication
@RestController
public class LoginpageApplication {
    HashMap<String, String> users = new HashMap<String, String>();
    @Autowired
    public ResourceLoader resourceLoader;
    private final static String SALT = BCrypt.gensalt();
    // Some fun things to include in your username/password!
    // TODO take from env cause yes
    public String flag = System.getenv("FLAG");
    public String randomNum = Integer.toString((int) (Math.random() * 100));
	// add more

    public static void main(String[] args) {
        SpringApplication.run(LoginpageApplication.class, args);
    }

    @GetMapping("/")
    public String getRoot(HttpServletResponse response) {
        try {
            response.sendRedirect("/register");
            return "Redirecting";
        } catch (Exception e) {
            return e.getMessage();
        }
    }

    @PostMapping("/register")
    public String postRegister(HttpServletResponse response, @RequestParam(value = "username") String username, @RequestParam(value = "password") String password) {
        try {
            if (username.isEmpty() || password.isEmpty()) return "No empty field";
            String tUsername = template(username);
            if (tUsername.contains(flag)) return "No flag >:( !";
            String tPassword = template(password);
            if (users.get(tUsername) != null) return "Username already taken!";
            users.put(tUsername, BCrypt.hashpw(tPassword, SALT));
            Cookie usernameCookie = new Cookie("username", Base64.getEncoder().encodeToString(tUsername.getBytes()));
            response.addCookie(usernameCookie);
            // yeah, sue me
            Cookie tokenCookie = new Cookie("token", BCrypt.hashpw(users.get(tUsername), SALT));
            response.addCookie(tokenCookie);
            response.sendRedirect("/hello");
            return "Redirecting";
        } catch (Exception e) {
            return e.getMessage();
        }
    }

    @GetMapping(value = "/register", produces = MediaType.TEXT_HTML_VALUE)
    public String getRegister() throws IOException {
        return resourceLoader.getResource("classpath:static/register.html").getContentAsString(Charset.defaultCharset());
    }

    @GetMapping("/hello")
    public String getHello(HttpServletResponse response, @CookieValue(value = "username", required = false) String username, @CookieValue(value = "token", required = false) String token) throws IOException {
        if (token == null || username == null) {
            response.sendRedirect("/login");
            return "Redirecting";
        }

        String decodedName = new String(Base64.getDecoder().decode(username));

        if (token.equals(BCrypt.hashpw(users.get(decodedName), SALT))) {
            return "Hello " + decodedName;
        } else {
            response.sendRedirect("/login");
            return "Redirecting";
        }
    }

    @PostMapping("/login")
    public String postLogin(HttpServletResponse response, @RequestParam(value = "username") String username, @RequestParam(value = "password") String password) {
        try {
            String actual = users.get(username);
            if (actual == null) return "Credentials wrong";

            String input = BCrypt.hashpw(password, SALT);
            if (input.equalsIgnoreCase(actual)) {
                Cookie usernameCookie = new Cookie("username", Base64.getEncoder().encodeToString(username.getBytes()));
                response.addCookie(usernameCookie);
                // yeah, sue me
                Cookie tokenCookie = new Cookie("token", BCrypt.hashpw(actual, SALT));
                response.addCookie(tokenCookie);

                response.sendRedirect("/hello");
                return "Redirecting";
            }
            response.setStatus(401);
			return "Credentials wrong";
        } catch (Exception e) {
            return e.getMessage();
        }
    }

    @GetMapping(value = "/login", produces = MediaType.TEXT_HTML_VALUE)
    public String getLogin() throws IOException {
        return resourceLoader.getResource("classpath:static/login.html").getContentAsString(Charset.defaultCharset());
    }


    private String template(String fmtStr) throws Exception {
        StringBuilder sb = new StringBuilder();
        while (fmtStr.contains("{{")) {
            int start = fmtStr.indexOf("{{") + 2;
            int end = fmtStr.indexOf("}}", start);
            if (end == -1) throw new Exception("Invalid Format String");
            sb.append(fmtStr, 0, start - 2);
            Field f = LoginpageApplication.class.getField(fmtStr.substring(start, end));
            if (f.getType().equals(String.class)) {
                sb.append(f.get(this));
            } else {
                throw new Exception("Field not found");
            }

            fmtStr = fmtStr.substring(end + 2);
        }
        // no format strings, no need.
        sb.append(fmtStr);
        return sb.toString();
    }

}
