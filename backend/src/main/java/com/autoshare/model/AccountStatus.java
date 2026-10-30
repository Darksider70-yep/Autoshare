package com.autoshare.model;

/**
 * Account verification and lifecycle state for User records.
 */
public enum AccountStatus {
    ACTIVE,
    VERIFIED,
    PENDING_KYC,
    SUSPENDED
}
