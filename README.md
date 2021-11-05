# vue-django-docker

This repo is an example application that uses Django (3.1.3) + Rest Framework (3.12.2) on the backend and Vue 3 + Typescript on the frontend. 
The app allows you to create users with different permissions, products, and view orders in a dashboard. 

The dashboard chart receives data from the 'chart/' endpoint and maps it using the c3.js library. 


# Steps to run:

## Backend

1. cd backend
2. docker-compose up

## Frontend

1. cd frontend
2. npm run serve
