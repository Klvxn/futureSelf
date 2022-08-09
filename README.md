# futureSelf

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

A simple clone of futureme.org that allows users send letters as emails to themselves in the future built with Django framework.

<p> Employed the use of a task queue like Celery and RabbitMQ as broker to run a periodic background task (sending emails to users on their scheduled date) </p>
