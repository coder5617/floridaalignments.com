# 🔒 Ubuntu Server Setup & Hardening Checklist
## Production Deployment for Florida Alignment & Suspension Website

Complete guide for setting up a secure, production-ready Ubuntu server for Flask application deployment.

---

## 📋 PRE-DEPLOYMENT REQUIREMENTS

### ✅ Prerequisites
- [ ] **Ubuntu Server 20.04 LTS or 22.04 LTS** instance ready
- [ ] **Root or sudo access** to the server
- [ ] **SSH key pair** generated on your local machine
- [ ] **Domain name** purchased and DNS configured
- [ ] **Basic server specs**: Minimum 1GB RAM, 1 CPU, 10GB storage

### ✅ Local Preparation
- [ ] **Git repository** with latest code ready to deploy
- [ ] **Environment configuration** file prepared (see BUSINESS_UPDATES_CHECKLIST.md)
- [ ] **Database backup/migration plan** if migrating existing data
- [ ] **SSL certificate plan** (Let's Encrypt recommended)

---

## 🚀 PHASE 1: INITIAL SETUP

### ✅ Step 1: User Account Setup
```bash
# Create dedicated application user
sudo adduser floridasuspension
sudo usermod -aG sudo floridasuspension

# Switch to app user for remaining setup
sudo su - floridasuspension
```

**Tasks:**
- [ ] Create non-root user for application
- [ ] Add user to sudo group
- [ ] Set strong password for the user
- [ ] Test sudo access

### ✅ Step 2: SSH Security
```bash
# Copy SSH key to server (run from LOCAL machine)
ssh-copy-id floridasuspension@your-server-ip

# Edit SSH configuration
sudo nano /etc/ssh/sshd_config
```

**SSH Configuration Changes:**
```bash
# Disable root login
PermitRootLogin no

# Disable password authentication (use keys only)
PasswordAuthentication no
PubkeyAuthentication yes

# Change default SSH port (optional - increases security through obscurity)
Port 2222

# Restrict users who can SSH
AllowUsers floridasuspension
```

**Tasks:**
- [ ] Copy SSH public key to server
- [ ] Disable root login
- [ ] Disable password authentication
- [ ] Test SSH key access
- [ ] Restart SSH service: `sudo systemctl restart ssh`

### ✅ Step 3: System Updates
```bash
# Update package lists and upgrade system
sudo apt update && sudo apt upgrade -y

# Install essential packages
sudo apt install -y \
    build-essential \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    git \
    curl \
    wget \
    unzip \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    gnupg \
    lsb-release

# Configure timezone
sudo timedatectl set-timezone America/New_York
```

**Tasks:**
- [ ] Update all system packages
- [ ] Install Python 3.8+ and development tools
- [ ] Install version control and web tools
- [ ] Set correct timezone for Orlando, FL
- [ ] Reboot if kernel was updated

---

## 🛡️ PHASE 2: SECURITY HARDENING

### ✅ Step 1: Firewall Configuration
```bash
# Configure UFW (Uncomplicated Firewall)
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow essential services
sudo ufw allow 2222/tcp    # SSH (if you changed the port)
sudo ufw allow ssh        # SSH (if using default port 22)
sudo ufw allow 80/tcp     # HTTP
sudo ufw allow 443/tcp    # HTTPS

# Enable firewall
sudo ufw enable

# Check status
sudo ufw status verbose
```

**Tasks:**
- [ ] Configure default firewall policies
- [ ] Allow only necessary ports
- [ ] Enable UFW firewall
- [ ] Verify firewall rules

### ✅ Step 2: Fail2Ban Setup
```bash
# Install Fail2Ban
sudo apt install fail2ban -y

# Create local configuration
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nano /etc/fail2ban/jail.local
```

**Fail2Ban Configuration:**
```ini
[DEFAULT]
# Ban IP for 10 minutes after 5 failed attempts
bantime = 600
findtime = 600
maxretry = 5

[sshd]
enabled = true
port = 2222    # Match your SSH port
logpath = /var/log/auth.log

[apache-badbots]
enabled = true
```

**Tasks:**
- [ ] Install and configure Fail2Ban
- [ ] Set up SSH protection
- [ ] Configure ban policies
- [ ] Start and enable service: `sudo systemctl enable fail2ban`

### ✅ Step 3: Automatic Security Updates
```bash
# Install unattended upgrades
sudo apt install unattended-upgrades -y

# Configure automatic updates
sudo dpkg-reconfigure --priority=low unattended-upgrades

# Edit configuration
sudo nano /etc/apt/apt.conf.d/50unattended-upgrades
```

**Configuration:**
```bash
# Enable security updates
Unattended-Upgrade::Automatic-Reboot "false";
Unattended-Upgrade::Automatic-Reboot-Time "02:00";
Unattended-Upgrade::Remove-Unused-Dependencies "true";
```

**Tasks:**
- [ ] Install unattended-upgrades package
- [ ] Enable automatic security updates
- [ ] Configure reboot policies
- [ ] Test configuration

### ✅ Step 4: System Monitoring
```bash
# Install system monitoring tools
sudo apt install htop iotop nethogs -y

# Install and configure auditd
sudo apt install auditd audispd-plugins -y

# Configure log monitoring
sudo nano /etc/audit/rules.d/audit.rules
```

**Audit Rules:**
```bash
# Monitor sensitive files
-w /etc/passwd -p wa -k passwd_changes
-w /etc/group -p wa -k group_changes
-w /etc/shadow -p wa -k shadow_changes
-w /etc/sudoers -p wa -k sudoers_changes

# Monitor system calls
-a always,exit -F arch=b64 -S execve -k exec_commands
```

**Tasks:**
- [ ] Install monitoring tools
- [ ] Configure audit daemon
- [ ] Set up file integrity monitoring
- [ ] Start audit service: `sudo systemctl enable auditd`

---

## 🗄️ PHASE 3: DATABASE SETUP

### ✅ PostgreSQL Installation & Configuration
```bash
# Install PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Start and enable PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create application database and user
sudo -u postgres createdb florida_alignment_production
sudo -u postgres createuser --interactive
```

**Database Setup:**
```sql
-- Connect as postgres user
sudo -u postgres psql

-- Create application user
CREATE USER florida_app WITH PASSWORD 'secure_password_here';

-- Create production database
CREATE DATABASE florida_alignment_production;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE florida_alignment_production TO florida_app;

-- Exit PostgreSQL
\q
```

**Tasks:**
- [ ] Install PostgreSQL server
- [ ] Create production database
- [ ] Create application database user
- [ ] Configure authentication
- [ ] Test database connection

### ✅ Database Security
```bash
# Configure PostgreSQL security
sudo nano /etc/postgresql/*/main/postgresql.conf
sudo nano /etc/postgresql/*/main/pg_hba.conf
```

**PostgreSQL Configuration:**
```bash
# postgresql.conf
listen_addresses = 'localhost'
port = 5432
max_connections = 100

# pg_hba.conf - Allow local connections only
local   all             postgres                                peer
local   all             all                                     md5
host    all             all             127.0.0.1/32            md5
```

**Tasks:**
- [ ] Restrict database connections to localhost
- [ ] Configure authentication methods
- [ ] Set up regular database backups
- [ ] Test connection security

---

## 🌐 PHASE 4: WEB SERVER SETUP

### ✅ Nginx Installation & Configuration
```bash
# Install Nginx
sudo apt install nginx -y

# Create application-specific configuration
sudo nano /etc/nginx/sites-available/florida-alignment
```

**Nginx Configuration:**
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    # SSL Configuration (Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;

    # Static files
    location /static/ {
        alias /home/floridasuspension/florida-alignment/app/static/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Application proxy
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**Tasks:**
- [ ] Install Nginx web server
- [ ] Create site-specific configuration
- [ ] Enable site configuration
- [ ] Test Nginx configuration: `sudo nginx -t`
- [ ] Start Nginx: `sudo systemctl start nginx`

### ✅ SSL Certificate Setup (Let's Encrypt)
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain SSL certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Test automatic renewal
sudo certbot renew --dry-run
```

**Tasks:**
- [ ] Install Certbot SSL manager
- [ ] Obtain SSL certificates for domain
- [ ] Configure automatic certificate renewal
- [ ] Test HTTPS configuration

---

## 🐍 PHASE 5: APPLICATION DEPLOYMENT

### ✅ Application Setup
```bash
# Clone application repository
cd /home/floridasuspension
git clone https://github.com/your-username/florida-alignment.git
cd florida-alignment

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install application dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn psycopg2-binary
```

**Tasks:**
- [ ] Clone application code from repository
- [ ] Create isolated Python virtual environment
- [ ] Install all application dependencies
- [ ] Install WSGI server (Gunicorn)

### ✅ Environment Configuration
```bash
# Create production environment file
nano .env
```

**Environment Variables:**
```bash
# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=production
SECRET_KEY=your-32-character-secret-key-here

# Database Configuration
DATABASE_URL=postgresql://florida_app:secure_password@localhost/florida_alignment_production

# Business Information
BUSINESS_NAME=Your Actual Business Name
BUSINESS_PHONE=(407) XXX-XXXX
BUSINESS_EMAIL=info@yourdomain.com
BUSINESS_ADDRESS=Your Real Address, Orlando, FL 32XXX

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-business@gmail.com
MAIL_PASSWORD=your-app-password

# Third-party Services
GOOGLE_MAPS_API_KEY=your-google-maps-api-key
GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX
```

**Tasks:**
- [ ] Create production environment file
- [ ] Set all required environment variables
- [ ] Generate secure secret key
- [ ] Configure email settings
- [ ] Set proper file permissions: `chmod 600 .env`

### ✅ Database Migration
```bash
# Activate virtual environment
source venv/bin/activate

# Initialize production database
flask init-db

# Test application
python app.py
```

**Tasks:**
- [ ] Initialize production database
- [ ] Run database migrations
- [ ] Load initial/sample data
- [ ] Test application locally on server

### ✅ Gunicorn WSGI Setup
```bash
# Test Gunicorn
gunicorn --bind 127.0.0.1:8000 app:app

# Create Gunicorn configuration
nano gunicorn.conf.py
```

**Gunicorn Configuration:**
```python
# gunicorn.conf.py
bind = "127.0.0.1:8000"
workers = 3
worker_class = "gevent"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 100
timeout = 30
keepalive = 2
preload_app = True
```

**Tasks:**
- [ ] Test Gunicorn WSGI server
- [ ] Create Gunicorn configuration
- [ ] Optimize worker settings for server specs

### ✅ Systemd Service Setup
```bash
# Create systemd service file
sudo nano /etc/systemd/system/florida-alignment.service
```

**Systemd Service Configuration:**
```ini
[Unit]
Description=Florida Alignment & Suspension Website
After=network.target

[Service]
User=floridasuspension
Group=floridasuspension
WorkingDirectory=/home/floridasuspension/florida-alignment
Environment=PATH=/home/floridasuspension/florida-alignment/venv/bin
EnvironmentFile=/home/floridasuspension/florida-alignment/.env
ExecStart=/home/floridasuspension/florida-alignment/venv/bin/gunicorn --config gunicorn.conf.py app:app
ExecReload=/bin/kill -s HUP $MAINPID
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

**Tasks:**
- [ ] Create systemd service file
- [ ] Enable service: `sudo systemctl enable florida-alignment`
- [ ] Start service: `sudo systemctl start florida-alignment`
- [ ] Check status: `sudo systemctl status florida-alignment`

---

## 📊 PHASE 6: MONITORING & LOGGING

### ✅ Log Configuration
```bash
# Create log directory
sudo mkdir -p /var/log/florida-alignment
sudo chown floridasuspension:floridasuspension /var/log/florida-alignment

# Configure log rotation
sudo nano /etc/logrotate.d/florida-alignment
```

**Log Rotation Configuration:**
```
/var/log/florida-alignment/*.log {
    daily
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    create 644 floridasuspension floridasuspension
    postrotate
        systemctl reload florida-alignment
    endscript
}
```

**Tasks:**
- [ ] Set up application logging
- [ ] Configure log rotation
- [ ] Monitor system logs
- [ ] Set up log monitoring alerts

### ✅ Performance Monitoring
```bash
# Install monitoring tools
sudo apt install htop iotop netstat-nat -y

# Set up basic monitoring script
nano /home/floridasuspension/monitor.sh
```

**Basic Monitoring Script:**
```bash
#!/bin/bash
# Basic server monitoring
echo "=== Server Status ===" > /tmp/server_status.txt
echo "Date: $(date)" >> /tmp/server_status.txt
echo "Uptime: $(uptime)" >> /tmp/server_status.txt
echo "Memory: $(free -h)" >> /tmp/server_status.txt
echo "Disk: $(df -h /)" >> /tmp/server_status.txt
echo "Service: $(systemctl is-active florida-alignment)" >> /tmp/server_status.txt

# Email report if service is down
if ! systemctl is-active --quiet florida-alignment; then
    mail -s "Florida Alignment Website Down" admin@yourdomain.com < /tmp/server_status.txt
fi
```

**Tasks:**
- [ ] Install monitoring tools
- [ ] Set up basic health checks
- [ ] Configure alert notifications
- [ ] Schedule monitoring cron jobs

---

## 💾 PHASE 7: BACKUP & RECOVERY

### ✅ Database Backup Setup
```bash
# Create backup script
nano /home/floridasuspension/backup_db.sh
chmod +x /home/floridasuspension/backup_db.sh
```

**Database Backup Script:**
```bash
#!/bin/bash
# Database backup script
BACKUP_DIR="/home/floridasuspension/backups"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="florida_alignment_production"

mkdir -p $BACKUP_DIR

# Create database backup
pg_dump -U florida_app -h localhost $DB_NAME | gzip > $BACKUP_DIR/db_backup_$DATE.sql.gz

# Keep only last 30 days of backups
find $BACKUP_DIR -name "db_backup_*.sql.gz" -mtime +30 -delete

echo "Database backup completed: db_backup_$DATE.sql.gz"
```

**Tasks:**
- [ ] Create automated backup script
- [ ] Set up daily database backups
- [ ] Configure backup retention policy
- [ ] Test backup restoration process

### ✅ File System Backup
```bash
# Create file backup script
nano /home/floridasuspension/backup_files.sh
chmod +x /home/floridasuspension/backup_files.sh
```

**File Backup Script:**
```bash
#!/bin/bash
# File system backup
BACKUP_DIR="/home/floridasuspension/backups"
DATE=$(date +%Y%m%d_%H%M%S)
APP_DIR="/home/floridasuspension/florida-alignment"

mkdir -p $BACKUP_DIR

# Backup application files (excluding venv and cache)
tar --exclude='venv' --exclude='__pycache__' --exclude='*.log' \
    -czf $BACKUP_DIR/files_backup_$DATE.tar.gz $APP_DIR

# Keep only last 14 days of file backups
find $BACKUP_DIR -name "files_backup_*.tar.gz" -mtime +14 -delete

echo "File backup completed: files_backup_$DATE.tar.gz"
```

### ✅ Automated Backup Schedule
```bash
# Set up cron jobs for automated backups
crontab -e
```

**Cron Configuration:**
```bash
# Daily database backup at 2 AM
0 2 * * * /home/floridasuspension/backup_db.sh >> /var/log/backups.log 2>&1

# Weekly file backup on Sundays at 3 AM
0 3 * * 0 /home/floridasuspension/backup_files.sh >> /var/log/backups.log 2>&1

# Daily health check at 6 AM
0 6 * * * /home/floridasuspension/monitor.sh
```

**Tasks:**
- [ ] Create automated backup scripts
- [ ] Schedule regular backups with cron
- [ ] Test backup and restore procedures
- [ ] Document recovery procedures

---

## 🔧 PHASE 8: FINAL OPTIMIZATION

### ✅ Performance Tuning
```bash
# Optimize Nginx for better performance
sudo nano /etc/nginx/nginx.conf
```

**Nginx Optimization:**
```nginx
# Worker processes = number of CPU cores
worker_processes auto;

# Optimize worker connections
events {
    worker_connections 1024;
    use epoll;
    multi_accept on;
}

http {
    # Enable gzip compression
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;

    # Cache static files
    location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

**Tasks:**
- [ ] Optimize Nginx worker configuration
- [ ] Enable gzip compression
- [ ] Configure static file caching
- [ ] Tune database connection pools

### ✅ Security Final Check
```bash
# Run security audit
sudo apt install lynis -y
sudo lynis audit system

# Check open ports
sudo netstat -tulpn | grep LISTEN

# Review running services
systemctl list-units --type=service --state=running
```

**Tasks:**
- [ ] Run system security audit
- [ ] Review open ports and services
- [ ] Remove unnecessary packages
- [ ] Verify all security measures

---

## ✅ DEPLOYMENT CHECKLIST

### 🎯 PRE-LAUNCH VERIFICATION

**Infrastructure:**
- [ ] **Server hardened** with firewall, Fail2Ban, SSH keys
- [ ] **Database** configured and secured with backups
- [ ] **Web server** running with SSL certificate
- [ ] **Application** deployed and running via systemd
- [ ] **Domain** pointing to server IP address
- [ ] **Monitoring** and alerting configured

**Security:**
- [ ] **SSH** access secured with key authentication only
- [ ] **Firewall** configured with minimal open ports
- [ ] **SSL certificate** installed and auto-renewing
- [ ] **Regular backups** scheduled and tested
- [ ] **Security updates** automated
- [ ] **Log monitoring** active

**Application:**
- [ ] **Environment variables** configured for production
- [ ] **Database migrations** completed successfully
- [ ] **Static files** served efficiently by Nginx
- [ ] **Email notifications** working correctly
- [ ] **API endpoints** functional and tested
- [ ] **Error pages** displaying correctly

**Performance:**
- [ ] **Load testing** completed successfully
- [ ] **Page load times** under 3 seconds
- [ ] **Mobile responsiveness** verified
- [ ] **SEO metadata** configured correctly
- [ ] **Analytics tracking** active

**Business:**
- [ ] **Contact information** updated with real data
- [ ] **Service descriptions** accurate and complete
- [ ] **Business hours** correct
- [ ] **Google Maps** showing correct location
- [ ] **Forms** submitting and sending emails properly

---

## 📞 POST-DEPLOYMENT TASKS

### ✅ Immediate Actions (First 24 Hours)
- [ ] **Monitor server resources** (CPU, memory, disk usage)
- [ ] **Check application logs** for errors
- [ ] **Verify all forms** are working correctly
- [ ] **Test email delivery** from contact forms
- [ ] **Submit sitemap** to Google Search Console
- [ ] **Set up Google My Business** profile

### ✅ Week 1 Tasks
- [ ] **Monitor website traffic** and performance
- [ ] **Check SSL certificate** status and expiration
- [ ] **Verify backup completion** daily
- [ ] **Review security logs** for anomalies
- [ ] **Test disaster recovery** procedures

### ✅ Ongoing Maintenance
- [ ] **Weekly security updates** review and application
- [ ] **Monthly performance** optimization review
- [ ] **Quarterly backup** restoration testing
- [ ] **Annual security audit** and penetration testing
- [ ] **Regular content updates** and SEO optimization

---

**🎉 Congratulations! Your Florida Alignment & Suspension website is now live and secure on a hardened Ubuntu server.**

**📝 Important Notes:**
- Keep all passwords and keys secure and backed up
- Document any custom configurations for future reference
- Regular maintenance is key to keeping the site secure and performant
- Consider professional monitoring services as the business grows

**🆘 Emergency Contacts:**
- Server Provider Support: [Your hosting provider's support contact]
- Domain Registrar Support: [Your domain provider's support contact]
- SSL Certificate Support: [Let's Encrypt community forums]