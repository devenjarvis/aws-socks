
<h3 align="center">socks</h3>

---

<p align="center"> 
    Most AWS tasks are solved problems. Stop reinventing the wheel.
    <br> 
</p>

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Usage](https://github.com/devenjarvis/aws-socks/wiki/Usage)
- [Contributing](/CONTRIBUTING.md)
- [Contributors](#contributors)
- [Roadmap](https://github.com/devenjarvis/aws-socks/wiki/Roadmap)

## 🧐 About <a name = "about"></a>
Current Version: 0.2.3

`socks` is a Python library designed to abstract common AWS tasks as one liners. It is opinionated in the pursuit to provide the most performant implementation that can be leveraged generally, but also attempts to offer reasonable levels of customization to the developer by supporting most boto3 functionality.

This package attempts to provide performant abstractions of the most common AWS tasks for the most common AWS services, so you can spend less time finding the best way to get that object from S3 and more time on what you actually want to do with that object (as an example).

This package is not comprehensive across all (or even most) AWS services at this time, but I hope to grow this overtime so a majority of the AWS tasks you find yourself re-solving or copying from one repo to the next can be implemented here in the most efficient way.


## 🏁 Getting Started <a name = "getting_started"></a>
Please note socks has not yet hit the 1.0 release so breaking API changes may occur. I'll try to limit those as possible and document them when they happen, but if you'd like to use socks it might be a good idea to lock your version in your requirements.txt file.

If you'd like to install the library locally or without code warp/spawn you can use the following install command:

`pip install aws-socks`

To upgrade an existing install use:

`pip install --upgrade aws-socks`

Once installed use `import socks` to start using it.

### Prerequisites
- The only external dependency for this library is boto3 which is packaged within the library.
- This package expects Python version 3.6 and up. There are no plans to support previous versions of Python.

## 🤠 Contributors <a name = "contributors"></a>
- [@jones-chris] (https://github.com/jones-chris) - Maintainer
- [@devenjarvis](https://github.com/devenjarvis) - Maintainer
- [@artkinghur](https://github.com/artkinghur) - SSM get_parameter exception handling
- [@arief-akbarr](https://github.com/arief-akbar) - Scan Dynamo Operation, Invoke Lambda Function
- [@ds0440](https://github.com/ds0440) - Support of boto3 kwargs