CREATE USER 'app' @'%' IDENTIFIED BY 'ead549a4a7c448926bfe5d0488e1a736798a9a8ee150418d27414bd02d37b9e5';
GRANT SELECT ON cps.* TO 'app' @'%';
GRANT INSERT ON cps.* TO 'app' @'%';
GRANT UPDATE (best_cps) ON cps.users TO 'app' @'%';
FLUSH PRIVILEGES;