package afras;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class AFRAS {

    public AFRAS() {
        JFrame frame = new JFrame("Face Recognition System");
        frame.setSize(1530, 820);
        frame.setLayout(null);

        // Background Panel
        JPanel bgPanel = new JPanel();
        bgPanel.setBounds(0, 0, 1530, 790);
        bgPanel.setLayout(null);
        frame.add(bgPanel);

        // Background Image
        ImageIcon bgIcon = new ImageIcon("images/bg4.jpg");
        Image scaledBgImage = bgIcon.getImage().getScaledInstance(1530, 790, Image.SCALE_SMOOTH);
        bgIcon = new ImageIcon(scaledBgImage);
        JLabel background = new JLabel(bgIcon);
        background.setBounds(0, 0, 1530, 790);
        bgPanel.add(background);

        // Title Label
        JLabel titleLabel = new JLabel("AUTOMATED FACE RECOGNITION ATTENDANCE SYSTEM");
        titleLabel.setFont(new Font("Arial", Font.BOLD, 30));
        titleLabel.setForeground(Color.WHITE);
        titleLabel.setBackground(Color.BLACK);
        titleLabel.setBounds(400, 0, 1530, 60);
        background.add(titleLabel);

        // Student Details Button
        JButton studentDetailsButton = new JButton();
        studentDetailsButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        studentDetailsButton.setBounds(200, 140, 220, 220);
        // Resize the icon
        ImageIcon studentIcon = new ImageIcon("images/student_details.png");
        Image scaledStudentIcon = studentIcon.getImage().getScaledInstance(220, 220, Image.SCALE_SMOOTH);
        studentIcon = new ImageIcon(scaledStudentIcon);
        studentDetailsButton.setIcon(studentIcon);
        background.add(studentDetailsButton);

        JButton studentDetailsTextButton = new JButton("Student Details");
        studentDetailsTextButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        studentDetailsTextButton.setFont(new Font("Arial", Font.BOLD, 15));
        studentDetailsTextButton.setForeground(Color.BLACK);
        studentDetailsTextButton.setBackground(Color.WHITE);
        studentDetailsTextButton.setBounds(200, 360, 220, 30);
        background.add(studentDetailsTextButton);
        
        
        ////////////////////////////////////////////////////////////
        studentDetailsButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    // Execute Python script
                    ProcessBuilder pb = new ProcessBuilder("python", "student.py");
                    pb.directory(new File("C:\\Users\\hardi\\Desktop\\AFRAS"));
                    Process p = pb.start();
                    BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                    String line;
                    while ((line = in.readLine()) != null) {
                        System.out.println(line);
                    }
                    in.close();
                } catch (IOException ex) {
                }
            }
        });
        ///////////////////////////////////////////////////////////

        // Face Detection Button
        JButton faceDetectionButton = new JButton();
        faceDetectionButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        faceDetectionButton.setBounds(600, 140, 220, 220);
        // Resize the icon
        ImageIcon faceDetectionIcon = new ImageIcon("images/face_detection.png");
        Image scaledFaceDetectionIcon = faceDetectionIcon.getImage().getScaledInstance(220, 220, Image.SCALE_SMOOTH);
        faceDetectionIcon = new ImageIcon(scaledFaceDetectionIcon);
        faceDetectionButton.setIcon(faceDetectionIcon);
        background.add(faceDetectionButton);

        JButton faceDetectionTextButton = new JButton("Detect Face");
        faceDetectionTextButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        faceDetectionTextButton.setFont(new Font("Arial", Font.BOLD, 15));
        faceDetectionTextButton.setForeground(Color.BLACK);
        faceDetectionTextButton.setBackground(Color.WHITE);
        faceDetectionTextButton.setBounds(600, 360, 220, 30);
        background.add(faceDetectionTextButton);
        
        ////////////////////////////////////////////////////////////
        faceDetectionButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    // Execute Python script
                    ProcessBuilder pb = new ProcessBuilder("python", "face_recognition.py");
                    pb.directory(new File("C:\\Users\\hardi\\Desktop\\AFRAS"));
                    Process p = pb.start();
                    BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                    String line;
                    while ((line = in.readLine()) != null) {
                        System.out.println(line);
                    }
                    in.close();
                } catch (IOException ex) {
                }
            }
        });
        ///////////////////////////////////////////////////////////

        // Attendance Button
        JButton attendanceButton = new JButton();
        attendanceButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        attendanceButton.setBounds(1000, 140, 220, 220);
        // Resize the icon
        ImageIcon attendanceIcon = new ImageIcon("images/attendance.png");
        Image scaledAttendanceIcon = attendanceIcon.getImage().getScaledInstance(220, 220, Image.SCALE_SMOOTH);
        attendanceIcon = new ImageIcon(scaledAttendanceIcon);
        attendanceButton.setIcon(attendanceIcon);
        background.add(attendanceButton);

        JButton attendanceTextButton = new JButton("Attendance");
        attendanceTextButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        attendanceTextButton.setFont(new Font("Arial", Font.BOLD, 15));
        attendanceTextButton.setForeground(Color.BLACK);
        attendanceTextButton.setBackground(Color.WHITE);
        attendanceTextButton.setBounds(1000, 360, 220, 30);
        background.add(attendanceTextButton);
        
        ////////////////////////////////////////////////////////////
        attendanceButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    // Execute Python script
                    ProcessBuilder pb = new ProcessBuilder("python", "attendance.py");
                    pb.directory(new File("C:\\Users\\hardi\\Desktop\\AFRAS"));
                    Process p = pb.start();
                    BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                    String line;
                    while ((line = in.readLine()) != null) {
                        System.out.println(line);
                    }
                    in.close();
                } catch (IOException ex) {
                }
            }
        });
        ///////////////////////////////////////////////////////////

        // Train Data Button
        JButton trainDataButton = new JButton();
        trainDataButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        trainDataButton.setBounds(200, 500, 220, 220);
        // Resize the icon
        ImageIcon trainDataIcon = new ImageIcon("images/train_data.png");
        Image scaledTrainDataIcon = trainDataIcon.getImage().getScaledInstance(220, 220, Image.SCALE_SMOOTH);
        trainDataIcon = new ImageIcon(scaledTrainDataIcon);
        trainDataButton.setIcon(trainDataIcon);
        background.add(trainDataButton);

        JButton trainDataTextButton = new JButton("Train Data");
        trainDataTextButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        trainDataTextButton.setFont(new Font("Arial", Font.BOLD, 15));
        trainDataTextButton.setForeground(Color.BLACK);
        trainDataTextButton.setBackground(Color.WHITE);
        trainDataTextButton.setBounds(200, 720, 220, 30);
        background.add(trainDataTextButton);
        
        ////////////////////////////////////////////////////////////
        trainDataButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    // Execute Python script
                    ProcessBuilder pb = new ProcessBuilder("python", "train.py");
                    pb.directory(new File("C:\\Users\\hardi\\Desktop\\AFRAS"));
                    Process p = pb.start();
                    BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                    String line;
                    while ((line = in.readLine()) != null) {
                        System.out.println(line);
                    }
                    in.close();
                } catch (IOException ex) {
                }
            }
        });
        ///////////////////////////////////////////////////////////

        // Photos Button
        JButton photosButton = new JButton();
        photosButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        photosButton.setBounds(600, 500, 220, 220);
        // Resize the icon
        ImageIcon photosIcon = new ImageIcon("images/photos.jpg");
        Image scaledPhotosIcon = photosIcon.getImage().getScaledInstance(220, 220, Image.SCALE_SMOOTH);
        photosIcon = new ImageIcon(scaledPhotosIcon);
        photosButton.setIcon(photosIcon);
        background.add(photosButton);

        JButton photosTextButton = new JButton("Photos");
        photosTextButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        photosTextButton.setFont(new Font("Arial", Font.BOLD, 15));
        photosTextButton.setForeground(Color.BLACK);
        photosTextButton.setBackground(Color.WHITE);
        photosTextButton.setBounds(600, 720, 220, 30);
        background.add(photosTextButton);
        
        ////////////////////////////////////////////////////////////
        photosButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    // Execute Python script
                    ProcessBuilder pb = new ProcessBuilder("python", "open.py");
                    pb.directory(new File("C:\\Users\\hardi\\Desktop\\AFRAS"));
                    Process p = pb.start();
                    BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
                    String line;
                    while ((line = in.readLine()) != null) {
                        System.out.println(line);
                    }
                    in.close();
                } catch (IOException ex) {
                }
            }
        });
        ///////////////////////////////////////////////////////////

        // Exit Button
        JButton exitButton = new JButton();
        exitButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        exitButton.setBounds(1000, 500, 220, 220);
        // Resize the icon
        ImageIcon exitIcon = new ImageIcon("images/exit.png");
        Image scaledExitIcon = exitIcon.getImage().getScaledInstance(220, 220, Image.SCALE_SMOOTH);
        exitIcon = new ImageIcon(scaledExitIcon);
        exitButton.setIcon(exitIcon);
        background.add(exitButton);

        JButton exitTextButton = new JButton("Exit");
        exitTextButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        exitTextButton.setFont(new Font("Arial", Font.BOLD, 15));
        exitTextButton.setForeground(Color.BLACK);
        exitTextButton.setBackground(Color.WHITE);
        exitTextButton.setBounds(1000, 720, 220, 30);
        background.add(exitTextButton);

        // Action Listeners for Buttons
        exitButton.addActionListener(new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Exit the application
            System.exit(0);
        }
        });
        // Student Details Button Action Listener

        // Similarly, add action listeners for other buttons

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        new AFRAS();
    }
}
