package com.example.springboot;

import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SoftwareEngineerService {

    private SoftwareEngineerRepo softwareEngineerRepo;

    public SoftwareEngineerService(SoftwareEngineerRepo softwareEngineerRepo) {
        this.softwareEngineerRepo = softwareEngineerRepo;
    }

    public List<SoftwareEngineer> getAllSoftwareEngineers(){
        return softwareEngineerRepo.findAll();
    }

    public void insertSoftwareEngineer(SoftwareEngineer softwareEngineer) {
        softwareEngineerRepo.save(softwareEngineer);
    }

    public SoftwareEngineer getSoftwareEngineerById(Integer id) {
        SoftwareEngineer softwareEngineer = softwareEngineerRepo.findById(id).orElseThrow(() -> new IllegalStateException(id + "not found"));
        return softwareEngineer;
    }
}
