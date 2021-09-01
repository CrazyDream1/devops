# CI best practices

## Git Actions

1. Keep your Actions minimal
2. Don’t install dependencies unnecessarily
3. Never hardcode secrets
4. Limit environment variables to the narrowest possible scope
5. Ensure every repository contains a CI/CD workflow
6. Store authors in Action metadata to promote code ownership
7. Don’t use self-hosted runners in a public repository

## Jenkins specific

1. Keep Jenkins Secure At All Times
2. Always Backup The “JENKINS_HOME” Directory
3. Setup A Different Job/Project For Each Maintenance Or Development Branch Created
4. Prevent Resource Collisions In Jobs That Are Running In Parallel
5. Use “File Fingerprinting” To Manage Dependencies
6. Build A Scalable Jenkins Pipeline
7. Manage Declarative Syntax/Declarative Pipelines
8. Manage Declarative Syntax/Declarative Pipelines
9. Maintain Higher Test Code Coverage & Run Unit Tests As Part Of Your Pipeline
10. Monitor Your CI/CD Pipeline
