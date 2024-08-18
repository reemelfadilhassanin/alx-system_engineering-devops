## Postmortem: Service Outage on ExApp

### Issue Summary:
- **Duration of the Outage:** August 17, 2024, 03:15 UTC to August 17, 2024, 06:00 UTC
- **Impact:** ExleApp's API service was down, leading to a complete outage of our API endpoints. This resulted in a service disruption for 100% of users. The outage caused failed API calls and service degradation, impacting both internal and external clients.
- **Root Cause:** A misconfiguration in the load balancer's routing rules caused a traffic bottleneck, which led to a cascade of failures across the API servers.

### Timeline:
- **03:15 UTC:** Issue detected when the monitoring system alerted on a high error rate and increased latency for API requests.
- **03:20 UTC:** Initial investigation showed that API endpoints were returning 500 Internal Server Errors. A customer complaint was also received about API downtime.
- **03:30 UTC:** Engineers began investigating the load balancer configuration and API server logs. It was initially suspected that the issue might be related to a recent deployment or a potential DDoS attack.
- **04:00 UTC:** Engineers determined that the issue was not related to recent deployments or external attacks but focused on load balancer settings.
- **04:30 UTC:** It was discovered that a routing rule change in the load balancer configuration was inadvertently directing all traffic to a single backend server, causing overload.
- **05:00 UTC:** The misconfiguration was corrected by reverting the load balancer settings to the previous, stable configuration.
- **05:30 UTC:** Service was restored, and normal operations resumed. Monitoring systems confirmed that the API errors and latency returned to normal levels.
- **06:00 UTC:** Full postmortem and root cause analysis completed. A follow-up review was scheduled to prevent future occurrences.

### Root Cause and Resolution:
- **Root Cause:** The outage was caused by a misconfigured routing rule in the load balancer. The rule change led to all incoming traffic being directed to a single API server, resulting in resource exhaustion and service downtime.
- **Resolution:** The configuration was reverted to the previous stable state. Additional checks were performed to ensure that all traffic was properly distributed across the API servers.

### Corrective and Preventative Measures:
- **Improvements Needed:**
  - **Configuration Management:** Implement stricter change management processes for configuration changes to avoid accidental misconfigurations.
  - **Monitoring Enhancements:** Improve monitoring to provide more granular alerts for changes in traffic distribution and server loads.
  - **Incident Response:** Enhance incident response procedures to include more detailed checks for configuration changes and their impact.

- **Tasks:**
  - Review and update the load balancer configuration management process.
  - Implement automated tests for configuration changes to detect potential issues before deployment.
  - Add alerts for traffic distribution anomalies and server load imbalances.
  - Conduct a review and update of the incident response playbook to include specific steps for handling configuration-related issues.

  
 ### Make people want to read your postmortem

We are constantly stormed by a quantity of information, it’s tough to get people to read you.
Make your post-mortem attractive by adding humour, a pretty diagram or anything that would catch your audience attention.