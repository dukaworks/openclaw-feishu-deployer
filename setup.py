#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦞 OpenClaw Feishu Deployer
一键部署 OpenClaw + 飞书机器人的专业工具
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="openclaw-feishu-deployer",
    version="1.0.3",
    author="Duka Works",
    author_email="chenzhy.bj@gmail.com",
    description="🦞 一键部署 OpenClaw + 飞书机器人的可爱工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dukaworks/openclaw-feishu-deployer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "openclaw-feishu=openclaw_feishu_deployer.cli:main",
            "ofd=openclaw_feishu_deployer.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
