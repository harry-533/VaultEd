document.addEventListener('DOMContentLoaded', function() {
    function setProgress(attendance, grade) {
        const attCircle = document.querySelector('.ring-fill-att');
        const attText = document.getElementById('percentage-text-att');
        const gradeCircle = document.querySelector('.ring-fill-grade');
        const gradeText = document.getElementById('percentage-text-grade');
    
        const radius = gradeCircle.r.baseVal.value;
        const circumference = 2 * Math.PI * radius;
    
        const attOffset = circumference - (attendance / 100) * circumference;
        const gradeOffset = circumference - (grade / 100) * circumference;
        gradeCircle.style.strokeDashoffset = gradeOffset;
        gradeCircle.style.stroke = getColor(grade);
        attCircle.style.strokeDashoffset = attOffset;
        attCircle.style.stroke = getColor(attendance);
    
        attText.textContent = `${attendance}%`;
        gradeText.textContent = `${grade}%`;
    }

    function getColor(percent) {
        if (percent < 20) return '#d80800'; 
        if (percent < 40) return '#ec6d0a'; 
        if (percent < 60) return '#fbda1b'; 
        if (percent < 80) return '#9bdb14'; 
        return '#0aa44b';
      };

    setProgress(95, 75);
})