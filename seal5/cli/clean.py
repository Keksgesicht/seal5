#
# Copyright (c) 2023 TUM Department of Electrical and Computer Engineering.
#
# This file is part of Seal5.
# See https://github.com/tum-ei-eda/seal5.git for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Command line subcommand for cleaning seal5 environment."""

from seal5.flow import Seal5Flow


def add_clean_options(parser):
    clean_parser = parser.add_argument_group("clean options")
    clean_parser.add_argument(
        "-n",
        "--name",
        metavar="NAME",
        nargs=1,
        type=str,
        default="default",
        help="Environment name (default: %(default)s)",
    )
    clean_parser.add_argument(
        "DIR",
        nargs="?",
        type=str,
        default=".",
        help="LLVM directory (default: %(default)s",
    )
    clean_parser.add_argument(
        "--temp",
        default=False,
        action="store_true",
        help="Delete temp folder folder?",
    )
    clean_parser.add_argument(
        "--patches",
        default=False,
        action="store_true",
        help="Delete patches folder folder?",
    )
    clean_parser.add_argument(
        "--models",
        default=False,
        action="store_true",
        help="Delete models folder folder?",
    )
    clean_parser.add_argument(
        "--inputs",
        default=False,
        action="store_true",
        help="Delete inputs folder folder?",
    )
    clean_parser.add_argument(
        "--logs",
        default=False,
        action="store_true",
        help="Delete logs folder folder?",
    )
    clean_parser.add_argument(
        "--install",
        default=False,
        action="store_true",
        help="Delete install folder folder?",
    )
    clean_parser.add_argument(
        "--build",
        default=False,
        action="store_true",
        help="Delete build folder folder?",
    )
    clean_parser.add_argument(
        "--deps",
        default=False,
        action="store_true",
        help="Delete deps folder folder?",
    )
    clean_parser.add_argument(
        "--non-interactive",
        dest="non_interactive",
        default=True,
        action="store_true",
        help="Do not ask questions interactively",
    )
    clean_parser.add_argument(
        "--verbose",
        default=False,
        action="store_true",
        help="Verbose printing of steps into console",
    )


def get_parser(subparsers):
    """ "Define and return a subparser for the clean subcommand."""
    parser = subparsers.add_parser("clean", description="clean Seal5 settings.")
    parser.set_defaults(func=handle)
    add_clean_options(parser)
    return parser


def handle(args):
    """Callback function which will be called to process the clean subcommand"""
    name = args.name[0] if isinstance(args.name, list) else args.name
    seal5_flow = Seal5Flow(args.DIR, name)
    seal5_flow.clean(
        temp=args.temp,
        patches=args.patches,
        models=args.models,
        inputs=args.inputs,
        logs=args.logs,
        install=args.install,
        build=args.build,
        deps=args.deps,
        verbose=args.verbose,
        interactive=not args.non_interactive,
    )
