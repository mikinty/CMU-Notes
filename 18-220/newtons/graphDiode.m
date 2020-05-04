IS = 1e-24;
vt = 0.025;
VIN = 8;
R = 10;

iD1 = @(vd) IS*(exp(vd/vt) - 1);
iD2 = @(vd) (VIN - vd)/R;

vDs = linspace(0, 1.4);

plot(vDs, iD1(vDs))
hold on
plot(vDs, iD2(vDs))