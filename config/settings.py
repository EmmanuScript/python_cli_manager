"""Configuration for task manager"""
import os
import json


class Config:
    """Base configuration"""
    DEBUG = False
    STORAGE_FILE = "tasks.dat"
    MAX_TASK_TITLE_LENGTH = 100
    ALLOWED_PRIORITIES = ["low", "medium", "high"]


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    STORAGE_FILE = "tasks_dev.dat"


class ProductionConfig(Config):
    """Production configuration"""
    STORAGE_FILE = os.environ.get("TASK_STORAGE_FILE", "/var/lib/tasks/tasks.dat")


def get_config():
    """Get current configuration"""
    env = os.environ.get("TASK_MANAGER_ENV", "development")
    if env == "production":
        return ProductionConfig()
    return DevelopmentConfig()
