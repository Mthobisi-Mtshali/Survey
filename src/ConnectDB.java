
//import com.sun.jdi.connect.spi.Connection;
import javax.swing.JOptionPane;
import java.sql.DriverAction;
import java.sql.*;


public class ConnectDB {
    Connection conn =null;
    
    public static Connection Connect()
    {
        try
        {
            Class.forName("com.mysql.cj.jdbc.Driver");
           Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mysql?zeroDateTimeBehavior=CONVERT_TO_NULL","root","");
            System.out.println("Connected Class");
            return conn;
        }
        catch(Exception e)
        {
            JOptionPane.showMessageDialog(null, e);
        }
        return null;
    }
    
}
