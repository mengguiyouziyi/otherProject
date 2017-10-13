package linshi_spider;

import org.jsoup.*;

import java.io.IOException;
import java.sql.*;
import java.sql.Connection;
import java.util.concurrent.*;

/**
 * Created by Administrator on 2017/6/8.
 */
public class web_jiance {
    public static void main(String args[]) throws ClassNotFoundException, IllegalAccessException, InstantiationException, SQLException {
        String driver1="com.mysql.jdbc.Driver";
        String url1="jdbc:mysql://etl2.innotree.org:3308/tyc?useUnicode=true&useCursorFetch=true&defaultFetchSize=100?useUnicode=true&characterEncoding=utf-8&tcpRcvBuf=1024000";
        String username="spider";
        String password="spider";
        Class.forName(driver1).newInstance();
        java.sql.Connection con=null;
        try {
            con = DriverManager.getConnection(url1, username, password);
        }catch (Exception e){
            while(true){
                con = DriverManager.getConnection(url1, username, password);
                if(con!=null){
                    break;
                }
            }
        }




        String url2="jdbc:mysql://etl1.innotree.org:3308/spider?useCursorFetch=true&defaultFetchSize=100&useUnicode=true&characterEncoding=utf-8&tcpRcvBuf=1024000";
        String username2="spider";
        String password2="spider";
        Class.forName(driver1).newInstance();
        java.sql.Connection con2=null;
        try {
            con2 = DriverManager.getConnection(url2, username2, password2);
        }catch (Exception e){
            while(true){
                con2 = DriverManager.getConnection(url2, username2, password2);
                if(con2!=null){
                    break;
                }
            }
        }


        web_jiance w=new web_jiance();
        final Cangku ca=w.new Cangku();
        final Xiugai xiu=w.new Xiugai();
        final Biao b=w.new Biao();
        final Connection finalCon1 = con2;
        ExecutorService pool= Executors.newCachedThreadPool();
        final Connection finalCon = con;
        pool.submit(new Runnable() {
            @Override
            public void run() {
                try {
                    data(finalCon1, ca);
                } catch (SQLException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        for(int x=1;x<=50;x++){
            pool.submit(new Runnable() {
                @Override
                public void run() {
                    try {
                        get(ca,xiu,b);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            });
        }


        pool.submit(new Runnable() {
            @Override
            public void run() {
                try {
                    xiudata(finalCon1,xiu);
                } catch (SQLException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        pool.submit(new Runnable() {
            @Override
            public void run() {
                try {
                    biaodata(finalCon1,b);
                } catch (SQLException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });



    }

    public static void get(Cangku ca,Xiugai xiu,Biao b) throws InterruptedException, IOException {
        while (true){
            String key[]=ca.qu();
            int a = 0;
            if(key!=null){
                String url = null;
                for(int x=1;x<=3;x++) {
                    try {
                        org.jsoup.Connection.Response doc = Jsoup.connect(key[1])
                                .ignoreContentType(true)
                                .ignoreHttpErrors(true)
                                .userAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
                                .method(org.jsoup.Connection.Method.GET)
                                .timeout(10000)
                                .execute();
                        a = doc.statusCode();
                        if (a==200) {
                            url=doc.url().toString();
                            break;
                        }
                    }catch (Exception e){

                    }
                }
                if(a!=200){
                    xiu.ru(new String[]{key[0],key[1]});
                }else{
                    b.ru(new String[]{key[0],url});
                }
            }else{
                Thread.sleep(10000);
                System.exit(0);
            }
        }
    }

    public static void data(Connection con,Cangku ca) throws SQLException, InterruptedException {
        String sql="select DISTINCT y_id,web from linshi_web_four";
        PreparedStatement ps=con.prepareStatement(sql);
        ResultSet rs=ps.executeQuery();
        while (rs.next()){
            String id=rs.getString(rs.findColumn("y_id"));
            String web=rs.getString(rs.findColumn("web"));
            ca.ru(new String[]{id,web});
        }
    }

    public static void xiudata(Connection con,Xiugai xiu) throws SQLException, InterruptedException {
        String sql="insert into linshi_web_four(y_id,web) values(?,?)";
        PreparedStatement ps=con.prepareStatement(sql);

        System.out.println("begin xiugai");
        int a=0;
        while (true){
            try {
                String[] upid = xiu.qu();
                if (upid != null) {
                    ps.setString(1, upid[0]);
                    ps.setString(2,upid[1]);
                    ps.executeUpdate();
                    a++;
                    System.out.println(a + "      " + "**********************************************");
                } else {
                    break;
                }
            }catch (Exception e){
                e.printStackTrace();
            }
        }
    }

    public static void biaodata(Connection con,Biao xiu) throws SQLException, InterruptedException {
        String sql="insert into linshi_web_five(y_id,web) values(?,?)";
        PreparedStatement ps=con.prepareStatement(sql);

        String sql2="delete from linshi_web_four where y_id=?";
        PreparedStatement ps2=con.prepareStatement(sql2);

        System.out.println("begin xiugai");
        int a=0;
        while (true){
            try {
                String upid[] = xiu.qu();
                if (upid != null) {
                    ps2.setString(1,upid[0]);
                    ps2.executeUpdate();
                    ps.setString(1,upid[0]);
                    ps.setString(2, upid[1]);
                    ps.executeUpdate();
                    a++;
                    System.out.println(a + "      " + "-------------------------------------------------------");
                } else {
                    break;
                }
            }catch (Exception e){
                e.printStackTrace();
            }
        }
    }

    class Cangku{
        BlockingQueue<String[]> ca=new LinkedBlockingQueue<String[]>();

        public void ru(String key[]) throws InterruptedException {
            ca.put(key);
        }

        public String[] qu() throws InterruptedException {
            return ca.poll(60, TimeUnit.SECONDS);
        }
    }

    class Xiugai{
        BlockingQueue<String[]> xiu=new LinkedBlockingQueue<String[]>();

        public void ru(String[] key) throws InterruptedException {
            xiu.put(key);
        }
        public String[] qu() throws InterruptedException {
            return xiu.take();
        }
    }

    class Biao{
        BlockingQueue<String[]> xiu=new LinkedBlockingQueue<String[]>();

        public void ru(String[] key) throws InterruptedException {
            xiu.put(key);
        }
        public String[] qu() throws InterruptedException {
            return xiu.take();
        }
    }

}
