def learn_theta(data, colors):
    max_blue = None

    for x, color in zip(data, colors):
        if color == "blue":
            if max_blue is None or x > max_blue:
                max_blue = x

    return float(max_blue)


def compute_ell(data, colors, theta):
    loss = 0

    for x, color in zip(data, colors):
        if color == "red" and x <= theta:
            loss += 1
        elif color == "blue" and x > theta:
            loss += 1

    return float(loss)


def minimize_ell(data, colors):
    best_theta = data[0]
    best_loss = compute_ell(data, colors, best_theta)

    for theta in data:
        loss = compute_ell(data, colors, theta)
        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return float(best_theta)


def minimize_ell_sorted(data, colors):
    n = len(data)

    total_blue = 0
    for color in colors:
        if color == "blue":
            total_blue += 1

    red_le_theta = 0
    blue_gt_theta = total_blue

    best_theta = data[0]
    best_loss = None

    for alpha in range(n):
        if colors[alpha] == "red":
            red_le_theta += 1
        else:
            blue_gt_theta -= 1

        loss = red_le_theta + blue_gt_theta

        if best_loss is None or loss < best_loss:
            best_loss = loss
            best_theta = data[alpha]

    return float(best_theta)
