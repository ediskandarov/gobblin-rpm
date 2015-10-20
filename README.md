gobblin-rpm
===========

A set of scripts to package gobblin into an RPM

Setup
-----

    $ sudo yum install git java-1.7.0-openjdk mock

Building
--------

    $ make

Resulting RPM will be avaliable at $(shell pwd)

Installing and operating
------------------------

    $ sudo yum install gobblin*.rpm

Libs, binaries, configs and logs are in /opt/gobblin.
