-- Oracle 21c Express Edition XE

create user OLTP identified by "YourPassword";
grant create session to AmazonStageKP;
grant all PRIVILEGES to AmazonStageKP;

create user AmazonStageKP identified by "YourPassword";
grant create session to AmazonStageKP;
grant all PRIVILEGES to AmazonStageKP;