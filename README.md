# no-dev-comments pre-commit hooks

***Work in progress***

## no-debug-inline-comments
Enforce that no inline `DEBUG` comments are left in code being pushed.
* Matches comments starting with ``#``, ``//``, ``"""``, or ``'''`` with the string ``DEBUG`` near the beginning.
* If the comment starts with ``"""`` or ``'''`` it must end with ``"""``, or ``'''``.
* Runs in `push` and `manual` stages by default.
* Applies to all `text` file types by default.

## no-fixme-inline-comments
Enforce that no inline `FIXME` comments are left in code being pushed.
* Matches comments starting with ``#``, ``//``, ``"""``, or ``'''`` with the string ``FIXME`` near the beginning.
* If the comment starts with ``"""`` or ``'''`` it must end with ``"""``, or ``'''``.
* Runs in `push` and `manual` stages by default.
* Applies to all `text` file types by default.

## no-testing-inline-comments
Enforce that no inline `TEST`` or ``TESTING` comments are left in code being pushed.
* Matches comments starting with ``#``, ``//``, ``"""``, or ``'''`` with the string ``TEST`` near the beginning.
* If the comment starts with ``"""`` or ``'''`` it must end with ``"""``, or ``'''``.
* Runs in `push` and `manual` stages by default.
* Applies to all `text` file types by default.

## no-debug-block-comments
Enforce that no `DEBUG` block comments are left in code being pushed.
* Matches block comments starting with ``#``, ``/*``, ``"""``, or ``'''`` with the string ``DEBUG`` near the beginning of the first or subsequent lines.
* If the comment starts with any of ``/*``, ``"""``, or ``'''`` it must end with any of ``*/``, ``"""``, or ``'''``.
* All lines in block comments starting with ``#`` must start with ``#`` (and/or spaces or tabs).
* Runs in `push` and `manual` stages by default.
* Applies to all `text` file types by default.

## no-fixme-block-comments
Enforce that no `FIXME` block comments are left in code being pushed.
* Matches block comments starting with ``#``, ``/*``, ``"""``, or ``'''`` with the string ``FIXME`` near the beginning of the first or subsequent lines.
* If the comment starts with any of ``/*``, ``"""``, or ``'''`` it must end with any of ``*/``, ``"""``, or ``'''``.
* All lines in block comments starting with ``#`` must start with ``#`` (and/or spaces or tabs).
* Runs in `push` and `manual` stages by default.
* Applies to all `text` file types by default.

## no-testing-block-comments
Enforce that no `TEST`` or ``TESTING` block comments are left in code being pushed.
* Matches block comments starting with ``#``, ``/*``, ``"""``, or ``'''`` with the string ``TEST`` near the beginning of the first or subsequent lines.
* If the comment starts with any of ``/*``, ``"""``, or ``'''`` it must end with any of ``*/``, ``"""``, or ``'''``.
* All lines in block comments starting with ``#`` must start with ``#`` (and/or spaces or tabs).
* Runs in `push` and `manual` stages by default.
* Applies to all `text` file types by default.
