package com.autoshare.dto;

import java.time.LocalDateTime;

public class BookingResponse {
    private final Long id;
    private final String studentName;
    private final String studentEmail;
    private final LocalDateTime bookedAt;

    public BookingResponse(Long id, String studentName, String studentEmail, LocalDateTime bookedAt) {
        this.id = id;
        this.studentName = studentName;
        this.studentEmail = studentEmail;
        this.bookedAt = bookedAt;
    }

    public Long getId() { return id; }
    public String getStudentName() { return studentName; }
    public String getStudentEmail() { return studentEmail; }
    public LocalDateTime getBookedAt() { return bookedAt; }
}
