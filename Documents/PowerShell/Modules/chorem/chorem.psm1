function chorem {
	param (
		$arg1,
		$arg2,
		$arg3
	)

	gsudo choco uninstall -y $arg1 $arg2 $arg3

	choco-package-list-backup 

}
