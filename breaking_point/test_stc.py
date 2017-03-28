#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.shell.core.context import ResourceCommandContext, ResourceContextDetails, ReservationContextDetails,ConnectivityContext
from driver import TestCenterControllerDriver
import thread



def create_context():
    context = ResourceCommandContext()
    context.resource = ResourceContextDetails()
    context.resource.name = 'TestCenter Controller 1'
    context.reservation = ReservationContextDetails()
    context.reservation.reservation_id = 'bc3aa7d1-7d66-4365-b419-65b90ece4d0f'
    context.reservation.owner_user = 'admin'
    context.reservation.owner_email = 'fake@qualisystems.com'
    context.reservation.environment_path ='config1'
    context.reservation.environment_name = 'config1'
    context.reservation.domain = 'Global'
    context.resource.attributes = {}
    context.resource.attributes['Client Install Path'] = 'C:\Program Files (x86)\Spirent Communications\Spirent TestCenter 4.52'
    context.resource.address = 'localhost'
    return context



if __name__ == '__main__':
    import time
    import threading
    context = create_context()
    driver = TestCenterControllerDriver()

    driver.initialize(context)


    response = driver.load_config(context,"C:\Users\luiza.n\Documents\configurationtest1.tcc","False")

    response = driver.start_devices(context)

    driver.start_traffic(context)

    response = driver.send_arp(context)

    response = driver.send_arp(context)


    driver.get_statistics(context,'generatorportresults', "json")

