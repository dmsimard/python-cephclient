#   Copyright 2013 David Moreau Simard
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   Author: David Moreau Simard <moi@dmsimard.com>
#


class FunctionNotImplemented(Exception):
    """
    Function not yet finished
    """
    def __str__(self):
        return "This function is not yet available/completed."


class UnsupportedRequestType(Exception):
    """
    If a requested body type is not mapped
    """
    def __str__(self):
        return "Unknown request type."


class UnsupportedBodyType(Exception):
    """
    If a requested body type is not mapped
    """
    def __str__(self):
        return "This type of body is not supported for this API call."
