func simplifyPath(path string) string {
	stack := []string{}
	names := strings.Split(path, "/")
	fmt.Println(names)
	for _, val := range names {
		if val == "." || val == "" {
			continue
		} else if val == ".." {
			if len(stack) > 0 {
				stack = stack[:len(stack)-1]
			}
		} else {
			stack = append(stack, val)
		}
	}
	canPath := "/" + strings.Join(stack, "/")
	return canPath
}
