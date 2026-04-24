import java.awt.*;
import java.util.*;
import java.lang.*;
import java.applet.*;

public class OCA extends java.applet.Applet {

        public void paint(Graphics g) {

                int Width = getSize().width;
                int Height = getSize().height;
        
                int w0 = 45;
                int w = 11*w0;
                int X0 = Width/2-(5*w0+w0/2)+10;
                int Y0 = Height/2;

                String s;
        
                int traits[] = new int[11];
                String traitname[] = {"x", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};

                String params = getParameter("traits");
                int i = 1;
                for (StringTokenizer t = new StringTokenizer(params, ","); t.hasMoreTokens() &&
i <= 10; ) {
                        traits[i++] = java.lang.Integer.valueOf(t.nextToken()).intValue();
                }

                // Set fore-/background colours
                setBackground(Color.yellow);
                setForeground(Color.black);

                g.setColor(Color.black);
                // Frame around total work area
                g.drawLine(0, 0, Width-2, 0);
                g.drawLine(Width-2, 0, Width-2, Height-2);
                g.drawLine(Width-2, Height-2, 0, Height-2);
                g.drawLine(0, Height-2, 0, 0);
        
                // Draw the grid
                for (int x = 0; x <= 11*w0; x += w0)
                        g.drawLine(X0+x, Y0-100, X0+x, Y0+100);
                for (i = 1; i < 11; i++)
                        g.drawString(traitname[i], X0+i*w0-2, Y0+115);
                for (int y = -100; y <= 100; y += 20) {
                        g.drawLine(X0, Y0-y, X0+w, Y0-y);
                        s = "   "+y;
                        s = s.substring(s.length()-4);
                        g.drawString(s, X0-30, Y0-y+4);
                }

                // Draw the lines between scores
                g.setColor(Color.red);
                for (i = 2; i < 11; i++)
                        g.drawLine(X0+(i-1)*w0, Y0-traits[i-1], X0+i*w0, Y0-traits[i]);
                // Draw circles round the points
                g.setColor(Color.blue);
                for (i = 1; i < 11; i++)
                        g.drawArc(X0+i*w0-4, Y0-traits[i]-4, 8, 8, 0, 360);

        }

        public String getAppletInfo() {
                return "Draws a graph for the OCA";
        }
}


