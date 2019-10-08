Vue.component('my_footer',{
    props: [],
    template: `<footer class="mastfoot pb-5 bg-white section-padding pb-0">
    <div class="inner container">
         <div class="row">
         	<div class="col-lg-4">
         		<div class="footer-widget pr-lg-5 pr-0">
                     {% for item in presentation %}
                     
         			<img src="{{ item.image.url }}" class="img-fluid footer-logo mb-3" alt="">
	         		<p>{{ item.description }}</p>
                     {% endfor %}
                     <nav class="nav nav-mastfoot justify-content-start">
                        {% for item in social %}
                            {% if forloop.first %}
                            <a class="nav-link" href="{{ item.lien }}">
                                <i class="fab fa-facebook-f"></i>
                            </a>
                            {% endif %}
                            {% if forloop.counter == 2 %}
                            <a class="nav-link" href="{{ item.lien }}">
                                <i class="fab fa-twitter"></i>
                            </a>
                            {% endif %}
                            {% if forloop.counter == 3 %}
                            <a class="nav-link" href="{{ item.lien }}">
                                <i class="fab fa-instagram"></i>
                            </a>
                            {% endif %}
                        {% endfor %}
		            </nav>
         		</div>
         		
         	</div>
         	<div class="col-lg-4">
         		<div class="footer-widget px-lg-5 px-0">
                     <h4>Open Hours</h4>
	         		<ul class="list-unstyled open-hours">
                         {% for item in horaires %}
		                <li class="d-flex justify-content-between"><span>{{ item.jour.jour }}</span><span>{{ item.start_hour }} - {{ item.end_hour }}</span></li>
		                {% endfor %}
		              </ul>
         		</div>
         		
         	</div>

         	<div class="col-lg-4">
         		<div class="footer-widget pl-lg-5 pl-0">
         			<h4>Newsletter</h4>
	         		<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
	         		<form id="newsletter">
						<div class="form-group">
							<input type="email" class="form-control" id="emailNewsletter" aria-describedby="emailNewsletter" placeholder="Enter email">
						</div>
						<button type="submit" class="btn btn-primary w-100">Submit</button>
					</form>
         		</div>
         		
         	</div>
         	<div class="col-md-12 d-flex align-items-center">
                 {% for item in presentation %}
                 <p class="mx-auto text-center mb-0">{{ item.license_site }}</p>
                 {% endfor %}
         	</div>
            
        </div>
    </div>
</footer>`
})