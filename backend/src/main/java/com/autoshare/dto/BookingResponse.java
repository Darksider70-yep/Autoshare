package com.autoshare.dto;

import java.time.LocalDateTime;

/**
 * DTO for outgoing booking information.
 */
public class BookingResponse {

    private Long id;
    private String studentName;
    private String studentEmail;
    private LocalDateTime bookedAt;

    public BookingResponse() {
    }

    public BookingResponse(Long id, String studentName, String studentEmail, LocalDateTime bookedAt) {
        this.id = id;
        this.studentName = studentName;
        this.studentEmail = studentEmail;
        this.bookedAt = bookedAt;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

    public String getStudentEmail() {
        return studentEmail;
    }

    public void setStudentEmail(String studentEmail) {
        this.studentEmail = studentEmail;
    }

    public LocalDateTime getBookedAt() {
        return bookedAt;
    }

    public void setBookedAt(LocalDateTime bookedAt) {
        this.bookedAt = bookedAt;
    }
}
