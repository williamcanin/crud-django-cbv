#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------------
#
# Description:

# Dj Tasks is a script to automate some tasks in Django project.
# These tasks at the moment are:
#   * Create .env file that distributes project environment variables.
#   * Creates the apps in a folder called apps.
# More information: https://github.com/williamcanin/dj-tasks

# License:

# MIT License

# Copyright (c) 2020-present - William C. Canin

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author: William Canin
# GitHub profile: https://github.com/williamcanin
# E-mail: william.costa.canin@gmail.com
# Home Page: https://williamcanin.github.io

from argparse import ArgumentParser
from os import getcwd
from os.path import isfile, isdir, join
from textwrap import dedent
from pathlib import Path
from subprocess import check_call, CalledProcessError


class Env:
    try:
        from django.utils.crypto import get_random_string
    except ImportError:
        print(
            ">>> It was not possible to import the Django module. "
            "Make sure that Django is installed."
        )
        exit(1)

    PATTERN = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"

    CONFIG_STRING = dedent(
        f"""
    DEBUG=True
    SECRET_KEY={get_random_string(50, PATTERN)}
    ALLOWED_HOSTS=.localhost, 127.0.0.1
    # DB_NAME=
    # DB_USER=
    # DB_PASSWORD=
    # DB_HOST=
    # DB_PORT=
    # # E.g URL postgresql: postgres://postgres:admin@localhost:5432/database
    # DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
    # DEFAULT_FROM_EMAIL=
    # EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    # EMAIL_HOST=
    # EMAIL_PORT=
    # EMAIL_USE_TLS=
    # EMAIL_HOST_USER=
    # EMAIL_HOST_PASSWORD=
    """
    ).strip()

    def write_env(self, file, msg=None):
        with open(file, "w") as content:
            content.write(self.CONFIG_STRING)
            print(msg)

    def create_env_file(self, file):
        msg = f"Done! Created {file} file."
        if isfile(file):
            reply = input(
                f"The file {file} already exists. "
                f"Do you want to overwrite? (y/N)\n-> "
            )
            if reply.lower() == "y":
                msg = f"Done! Overwrite {file} file."
                self.write_env(file, msg=msg)
                return
            print("Aborted!")
            return
        self.write_env(file, msg=msg)


class App:
    @staticmethod
    def create_dir(directory):
        directory = f"apps/{directory}"
        path = Path(directory)
        path.mkdir(exist_ok=True, parents=True)

    def create_app(self, app_name):
        self.create_dir(app_name)
        try:
            check_call(
                f"python manage.py startapp {app_name} apps/{app_name}", shell=True
            )
            success_create = dedent(f"""

            App "./apps/{app_name}" created!

            Now, in "settings.py", installed your app:

            INSTALLED_APPS = [
                ...
                "apps.{app_name}",
                ...
            ]
            """).strip()
            print(success_create)
        except (CalledProcessError):
            if not isdir(f"./apps/{app_name}"):
                print(">>> There was an error creating the app. Aborted.")


class DjTasks(Env, App):
    @staticmethod
    def options(run_help=None):
        parser = ArgumentParser(description="Automate commands and tasks.")
        parser.add_argument(
            "--env",
            action="store_true",
            help='creates ".env" file for environment variables.',
        )

        parser.add_argument(
            "--app",
            metavar="APP NAME",
            help='create a new application in the "apps" folder.',
        )

        args = parser.parse_args(run_help)

        return args

    def main(self):
        if not isfile(join(getcwd(), "manage.py")):
            return print(">>> It is not in a Django project.")
        if self.options().env:
            self.create_env_file(".env")
        elif self.options().app:
            self.create_app(self.options().app)
        else:
            run_help = ["--help"]
            print(self.options(run_help))


if __name__ == "__main__":
    DjTasks().main()
