package com.autoshare.dto;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;

public class BookingRequest {

    @NotBlank(message = "Student name is required")
    private String studentName;

    @NotBlank(message = "Student email is required")
    @Email(message = "Student email must be a valid email address")
    private String studentEmail;

    public BookingRequest() { }

    public BookingRequest(String studentName, String studentEmail) {
        this.studentName = studentName;
        this.studentEmail = studentEmail;
    }

    public String getStudentName() { return studentName; }
    public void setStudentName(String studentName) { this.studentName = studentName; }
    public String getStudentEmail() { return studentEmail; }
    public void setStudentEmail(String studentEmail) { this.studentEmail = studentEmail; }
}
