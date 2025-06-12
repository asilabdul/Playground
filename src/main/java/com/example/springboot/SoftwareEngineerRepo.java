package com.example.springboot;

import org.springframework.data.jpa.repository.JpaRepository;

public interface SoftwareEngineerRepo
        extends JpaRepository<SoftwareEngineer, Integer> {
}
