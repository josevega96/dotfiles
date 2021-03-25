function bareconf {
	param(
	 	$arg1,
		$arg2,
		$arg3,
		$arg4,
		$arg5
	)
	git --git-dir=$env:USERPROFILE/.cfg/ --work-tree=$env:USERPROFILE $arg1 $arg2 $arg3 $arg4 $arg5 
}
