function choin {
	param (
		$arg1,
		$arg2,
		$arg3
	)

	gsudo choco install -y $arg1 $arg2 $arg3

	choco-package-list-backup 

}
